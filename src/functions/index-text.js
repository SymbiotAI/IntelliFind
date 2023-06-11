const {RecursiveCharacterTextSplitter} = require("langchain/text_splitter");
const {Document} = require("langchain/document");
const {OpenAIEmbeddings} = require("langchain/embeddings");
const {Chroma} = require("langchain/vectorstores");

module.exports.indexText = async (text) => {
    const textSplitter = new RecursiveCharacterTextSplitter({
        chunkSize:1000,
        chunkOverlap:60
    })

    const doc = new Document({
        pageContent:text
    })

    const docs = textSplitter.splitDocuments([doc])

    const embeddings = new OpenAIEmbeddings()

    const db = await Chroma.fromDocuments(docs,embeddings,{
        url:'',
        collectionName:''
    })
}
