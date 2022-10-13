const express = require('express');
const { engine } = require('express-handlebars');
const { create } = require('express-handlebars');
const bodyparser = require('body-parser');
const path = require('path');
const app = express();

const fakedata = [
    {
        id: 1,
        nome: 'Zezinho',
        endereco: 'Rua lalalal 100',
        telefone: '5555-1234',
        cancelado: 'nao'
    },
    {
        id: 2,
        nome: 'Huguinho',
        endereco: 'Rua lululul 200',
        telefone: '5555-4321',
        cancelado: 'sim'
    }
];
/*Configura a engine (motor) do express para utilizar o handlebars */
app.use(bodyparser.urlencoded({extended: false}));
app.set('view engine','handlebars');
app.engine('handlebars', engine());

create({}).handlebars.registerHelper('checked', function(value, test) {
    if (value == undefined) return '';
    return value==test ? 'checked' : '';
});
/*disponibilizando acesso para as bibliotecas estaticas do bootstrap e jquery */
app.use('/css', express.static(path.join(__dirname, 'node_modules/bootstrap/dist/css')));
app.use('/js', express.static(path.join(__dirname, 'node_modules/bootstrap/dist/js')));
app.use('/js', express.static(path.join(__dirname, 'node_modules/jquery/dist')));
app.use('/public', express.static(path.join(__dirname, 'public')));

app.get('/', function(req,res){
    //res.send("<h1>eu nao acredito</h1>");
    res.render('index');
});

app.get('/membros/delete/:id', function(req,res){
    let ummembros = fakedata.find(o => o.id == req.params['id']);
    let index = fakedata.indexOf(ummembros);
    if (index > -1){
        fakedata.splice(index,1);
    }
    res.render('membros/membros',{data: fakedata});
});


app.get('/membros/novo', function(req,res){
    res.render('membros/formmembros');
});

app.get('/membros/alterar/:id', function(req,res){
    let idmembros = req.params['id'];
    let ummembros = fakedata.find( o => o.id == idmembros);
    
    res.render('membros/formmembros', {membro: ummembros});
    
});



app.post('/membros/save', function(req,res){
    let membrosantigo = fakedata.find(o => o.id == req.body.id);

    if(membrosantigo != undefined){
        /*ALTERAR */
        membrosantigo.nome = req.body.nome;
        membrosantigo.cidade = req.body.cidade;
        membrosantigo.telefone = req.body.telefone;
        membrosantigo.idade = req.body.idade;
        membrosantigo.ocupacao = req.body.ocupacao;
        membrosantigo.vezesqueassistiu = req.body.vezesqueassistiu;
        membrosantigo.contribuicao = req.body.contribuicao;
    }else{
        /*INCLUIR */
        let maxid = Math.max(...fakedata.map( o => o.id));
        if (maxid == -Infinity) maxid = 0;

        let novomembros = {
            nome: req.body.nome,
            cidade: req.body.cidade,
            telefone: req.body.telefone,
            idade: req.body.idade,
            ocupacao: req.body.ocupacao,
            vezesqueassistiu: req.body.vezesqueassistiu,
            contribuicao: req.body.contribuicao,
            id: maxid + 1,
        };
        fakedata.push(novomembros);
    }
    res.redirect("/membros");
});


app.get('/membros', function(req,res){
    //res.send("<h1>eu nao acredito</h1>");
    res.render('membros/membros', {listamembros: fakedata});
});

/*inicialização da aplicação NodeJS + Express */
app.listen(3000, () =>{
    console.log('Server online - http://localhost:3000/');
});
