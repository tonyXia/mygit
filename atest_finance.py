# coding=utf-8

from framework.base_page import BasePage

class FinancePage(BasePage):
    #点击财务
    clickfinance = "link_text=>财务"

    #点击应收款名
    receviableMoney = "id=>name"
    #点击合同名
    contract = "id=>contract_name"
    #找到需要找到的合同号并且选择

    def click_contractNO(self,contractNO):
        clickcontractNOs = self.driver.find_elements_by_xpath("//tbody[@id='datas']/tr/td[2]")
			for clickcontractNO in clickcontractNOs:
				if contractNO == clickcontractNO.text:
					path = "xpath=>../td[1]/input[@name='contract']"
					return path
					
					


    def click_viewer(self,names):
        clickdatas = self.driver.find_elements_by_xpath("//tbody[@id='datas']/tr/td[2]")
		for clickdata in clickdatas:
			if names == clickdata:
				path = "xpath=>../td[1]/input[@name='customer']"
				return path
					

    def click_admin(self, names):
        clickadmins = self.driver.find_elements_by_xpath("//tbody[@id='d_content']/tr/td[2]")
			for clickdata in clickadmins:
				if names == clickdata:
					path = "xpath=>../td[1]/input[@name='owner_id']"
					return path
		
	
	
	#悬停
	mouseshow = dr.find_element_by_link_text("仪表盘")
	ActionChains(dr).move_to_element(mouseshow).perform()
	dr.implicitly_wait(10)

    price = "id=>price"

    payTime = "id=>pay_time"

    description = "class=>span6"
    field = "id=>field&index=2"

    submitbtn = "xpath=>//thead/tr/td[2]/input[1]"
	
	





