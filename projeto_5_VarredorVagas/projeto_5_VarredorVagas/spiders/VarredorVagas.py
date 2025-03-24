# site https://www.catho.com.br/ e varra vagas com a palavra chave python
# cargo
# nome empresa
# local
# link para a vaga

import scrapy


class VagasPythonSpider(scrapy.Spider):
    # identidade
    name = 'vagasbot'

    # Request
    def start_requests(self):
        urls = ['https://www.catho.com.br/vagas/python/?page=1']

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, meta={'page': 1}, errback=self.erro_pag)

    # Response

    def parse(self, response):
        seen = set()
        pagina_atual = response.meta['page']

        self.logger.info(f"-----> Processando a página {pagina_atual} <-----")

        vagas = response.xpath("//li//article//header//div")
        if vagas:
            for item in vagas:
                cargo = item.xpath(".//h2/a/text()").get()
                nome_empresa = item.xpath(".//p/text()").get()
                local = item.xpath(".//div//button/a/text()").get()
                link = item.xpath(".//h2/a/@href").get()

                # Verificação de duplicadas
                if cargo and link and (cargo, link) not in seen:
                    seen.add((cargo, link))
                    yield {
                        'cargo': cargo,
                        'nome empresa': nome_empresa,
                        'local': local,
                        'link': link
                    }

            # Próxima página
            proxima_pagina = pagina_atual + 1
            proxima_pagina_url = f"https://www.catho.com.br/vagas/python/?page={proxima_pagina}"
            self.logger.info(
                f"-----> Fim da Varredura da página: {pagina_atual} <-----")

            yield scrapy.Request(url=proxima_pagina_url, callback=self.parse, meta={'page': proxima_pagina}, errback=self.erro_pag)
        else:
            self.logger.info(f"Estamos na última página: {pagina_atual}")

    # Erros em paginas
    def erro_pag(self, failure):
        pagina_atual = failure.request.meta['page']
        self.logger.error(
            f"Erro ao processar a página {pagina_atual}: {failure.value}")

        # Continuar para a próxima página
        proxima_pagina = pagina_atual + 1
        proxima_pagina_url = f"https://www.catho.com.br/vagas/python/?page={proxima_pagina}"
        self.logger.info(f"Pulando para a próxima página: {proxima_pagina}")
        yield scrapy.Request(url=proxima_pagina_url, callback=self.parse, meta={'page': proxima_pagina}, errback=self.erro_pag)
