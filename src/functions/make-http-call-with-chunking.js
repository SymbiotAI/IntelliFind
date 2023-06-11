const {chunk} = require('./chunk');
const axios = require('axios');
module.exports.makeHttpCallWithChunkings = async (input,apiKey) =>{
    const chunks = chunk(input,1000)
    const responseChunks = []
    for(const ch in chunks){
        const payload = {
            input:ch,
            model:'text-embedding-ada-002'
        }

        const response = await axios.post('https://api.openai.com/v1/embeddings',JSON.stringify(payload),{
            headers:{
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + apiKey
            }
        })

        responseChunks.push(response.data)

    }

    return responseChunks.join('')
}
