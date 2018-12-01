# -*- coding: utf-8 -*-
from urllib import quote

helpmsg ='''------MCD wiki插件------
!!wiki [搜索内容] -搜索mc wiki
--------------------------------'''

def onServerInfo(server, info):
  if info.isPlayer == 1:
    if info.content.startswith('!!wiki'):
      args = info.content.split(' ')
      if (len(args) == 1):
        for line in helpmsg.splitlines():
          server.tell(info.player, line)
      elif (len(args) == 2):
        search = 'tellraw ' + info.player + ' {"text":"[wiki]: 搜索' + args[1] + '的结果","underlined":"true","clickEvent":{"action":"open_url","value":"https://minecraft-zh.gamepedia.com/index.php?search=' + quote(args[1]) + '"}}'
        server.execute(str(search))
      else:
        server.tell(info.player, '参数不正确')