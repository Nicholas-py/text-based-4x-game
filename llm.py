import lmstudio as lms
from time import time

client = lms.AsyncClient()

models = ['qwen3-8b','liquid/lfm2-1.2b']

syncmodel = lms.llm(models[0])
async def asyncresponse(message):
    raise NotImplemented()
    with lms.AsyncClient() as client:
        model  = await client.llm.model('liquid/lfm2-1.2b')
        return (await model.respond(message))
        
def syncresponse(message):
    print('Awaiting model response')
    pretime = time()
    result = syncmodel.respond(message+' /no_think')
    print('Done in',time()-pretime,'seconds')
    result = str(result).replace('<think>','')
    result = result.replace('</think>','')
    return str(result)