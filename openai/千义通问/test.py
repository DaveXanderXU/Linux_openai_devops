# For prerequisites running the following sample, visit https://help.aliyun.com/document_detail/611472.html

import dashscope
from dashscope import Generation
from http import HTTPStatus
import json

dashscope.api_key='sk-1346c0ea97264b38b942bde771fbdae5'

responses=Generation.call(
    model='qwen-v1',
    prompt='就当前的海洋污染的情况，写一份限塑的倡议书提纲，需要有理有据地号召大家克制地使用塑料制品',
    stream=True)

for response in responses:
    if response.status_code==HTTPStatus.OK:
        print(json.dumps(response.output, indent=4, ensure_ascii=False))
    else:
        print('Code: %d, status: %s, message: %s' % (response.status_code, response.code, response.message))


        