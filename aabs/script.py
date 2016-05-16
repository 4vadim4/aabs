#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging



def log_func(request):
    logging.basicConfig(format = '%(levelname)-8s [%(asctime)s] %(message)s', level = logging.INFO, filename = 'logger1.log')
#    remote_addr = request.META.get('REMOTE_ADDR', 'Значение IP не найдено')
#    logname = request.META.get('LOGNAME', 'Имя пользователя не найдено')
#    http_user_agent = request.META.get('HTTP_USER_AGENT', 'Имя HTTP агента не найдено')
#    logging.info(logname, '-', remote_addr, '-', http_user_agent)
 #   logging.info(str(logname), '-', str(remote_addr), '-', str(http_user_agent))




    logging.info('%s, %s, %s, \n\t%s' % (request.META['REMOTE_ADDR'], request.META['LOGNAME'],
                                      request.META['PATH_INFO'], request.META['HTTP_USER_AGENT']))