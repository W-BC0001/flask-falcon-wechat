## about open-falcon alarm
- open-falcon alarm可以调用http接口发送报警信息
- alarm一般是post发送数据至报警插件，post数据一般是dict类型，包含两个key(content，tos)，并且value都是unicode类型
- post data举例
  - {('content', [u'2', u'old.gen.mem.ratio', u'e.g.', u'test-host', u'test-information', u'']), ('tos', 'someuser')}
  - {('content', [P0][OK][test-host][][errmsg  0>0][O1 2020-08-14 11:32:00]), ('tos', 'someuser')}