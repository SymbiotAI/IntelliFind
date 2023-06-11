const {makeHttpCallWithChunkings} = require("../../functions/make-http-call-with-chunking");
module.exports = {
    handler:async (event) =>{
        try {
            console.log(process.env.EMBDEDDINGS_OPENAI_API_KEY)
            const result = await makeHttpCallWithChunkings(event.body,process.env.EMBDEDDINGS_OPENAI_API_KEY)
            console.log(result)
            return {
                statusCode:200

            }
        } catch (e){
            console.log(e)
            return {
                statusCode:500

            }
        }

    }
}
