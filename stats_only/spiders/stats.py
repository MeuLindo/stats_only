import scrapy


class StatsSpider(scrapy.Spider):
    name = 'stats'
    allowed_domains = ['https://www.hltv.org/results']
    start_urls = ['https://www.hltv.org/matches/2345600/fenrir-vs-forbidden-esea-mdl-season-35-australia-relegation']

    def parse(self, response):
        
        time1 = response.xpath("/html/body/div[2]/div/div[2]/div[1]/div[2]/div[1]/div[1]/div/a/div/text()").get()
        score_team_1 = response.xpath("/html/body/div[2]/div/div[2]/div[1]/div[2]/div[1]/div[1]/div/div/text()").get()
        time2 = response.xpath("/html/body/div[2]/div/div[2]/div[1]/div[2]/div[1]/div[3]/div/a/div/text()").get()
        score_team_2 = response.xpath("/html/body/div[2]/div/div[2]/div[1]/div[2]/div[1]/div[3]/div/div/text()").get()
        times = {
            "time1" : time1 ,
            "score_team_1" : score_team_1 ,
            "time2" : time2 ,
            "score_team_2" : score_team_2
            }
        
        
        data = response.xpath("/html/body/div[2]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/text()").get()
        hora = response.xpath("/html/body/div[2]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/text()").get()
        agenda = {"data" : data, "hora" : hora}

        descricao = response.xpath("/html/body/div[2]/div/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]/div/text()").get()
        
        print(times, descricao, agenda)
