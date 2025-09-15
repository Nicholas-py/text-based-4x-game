import lmstudio as lms

client = lms.AsyncClient()
#model = client.llm.model('liquid/lfm2-1.2b')
syncmodel = lms.llm('liquid/lfm2-1.2b')
async def asyncresponse(message):
    with lms.AsyncClient() as client:
        model  = await client.llm.model('liquid/lfm2-1.2b')
        return (await model.respond(message))
        
def syncresponse(message):
    result = syncmodel.respond(message)
    return str(result)