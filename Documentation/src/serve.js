import express from "express"
import { dirname } from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const app = express()
console.log(__dirname)
app.use('/', express.static(__dirname + '/public'));
app.listen(3333, () => {
    console.log("Servidor rodando http://localhost:3333")
})