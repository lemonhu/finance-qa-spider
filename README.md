# 基于Scrapy框架的金融问答文本数据库建设
---
## 开发语言
Python
## 开发平台
Eclipse+Pydev
## 数据来源
1. 上交所官方平台的问答系统  
   http://sns.sseinfo.com/qa.do  

2. 深交所官方平台的问答系统  
   http://irm.cninfo.com.cn/szse/index.html　　

3. 全景网投资者关系互动平台  
   http://rs.p5w.net/index/company/showQuestionPage.shtml　　

4. 新浪股吧  
   http://guba.sina.com.cn/?s=channel&chi
## 数据库表shse_qa
	mysql> CREATE TABLE IF NOT EXISTS `shse_qa`(
	    -> `current_time` TIMESTAMP NOT NULL,
	    -> `user_name` VARCHAR(100) NOT NULL,
	    -> `company_name` VARCHAR(100) NOT NULL,
	    -> `company_id` int(20) NOT NULL,
	    -> `question_time` VARCHAR(100) NOT NULL,
	    -> `question_content` text NOT NULL,
	    -> `answer_time` VARCHAR(100),
	    -> `answer_content` text
	    -> )ENGINE=InnoDB DEFAULT CHARSET=utf8;