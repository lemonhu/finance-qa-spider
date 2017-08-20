# -*- coding: utf-8 -*-
from MySQLdb import cursors
import MySQLdb
from twisted.enterprise import adbapi
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class FinanceQaSpiderPipeline(object):
    
    def __init__(self, dbpool):
        self.dbpool = dbpool
        
    @classmethod
    def from_settings(cls, settings):
        dbparams = dict(
            host=settings['MYSQL_HOST'],
            port=settings['MYSQL_PORT'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            db=settings['MYSQL_DB'],
            charset='utf8',
            use_unicode=True,
            cursorclass=MySQLdb.cursors.DictCursor,
            )
        
        dbpool = adbapi.ConnectionPool('MySQLdb', **dbparams)
        return cls(dbpool)
    
    # pipeline默认调用
    def process_item(self, item, spider):
        query=self.dbpool.runInteraction(self._conditional_insert, item) #调用插入的方法
        query.addErrback(self._handle_error, item, spider) #调用异常的处理方法
        return item
    
    # 写入到数据库中
    def _conditional_insert(self, tx, item):
        sql = 'INSERT INTO shse_qa(user_name, company_name, company_id, question_time, question_content, answer_time, answer_content) VALUES(%s, %s, %s, %s, %s, %s, %s)'
        params = (item['user_name'], item['company_name'], item['company_id'], item['question_time'], item['question_content'], item['answer_time'], item['answer_content'])
        tx.execute(sql, params)
        
        print 'user_name:' + item['user_name']
        
    # 错误处理方法
    def _handle_error(self, failue, item, spider):
        print failue