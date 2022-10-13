<html>
  <head>
    <title>Formulário</title>
  </head>
  <body>
    <form action="processa.php" method="POST">
      <!-- Fieldset e legend são obrigatorios-->
      <fieldset>
        <legend>Dados Pessoais</legend>
        <p>
          <label for="nome">Nome:</label>
          <input type="text" name="txtnome" 
            id="nome" placeholder="Digite seu nome completo">
          <input type="hidden" name="secreto" value="1234" required>
        </p>
        <p>
          <label for="email">Email:</label>
          <input type="email" name="txtemail" id="email" required>
        </p>
        <p>
          <label for="senha">Senha:</label>
          <input type="password" name="txtsenha" id="senha" required>
        </p>
        <p>
          <label for="date">Data:</label>
          <input type="date" name="txtdata" id="data">
        </p>
        <p>
          <label for="cor">Cor:</label>
          <input type="color" name="txtcor" id="cor">
        </p>
        <p>
          <label for="checkidade">Maior de Idade:</label>
          <input type="checkbox" name="cbidade" id="checkidade" required>
        </p>
        <p>
          <label for="radiocidade">Mora em Joinville:</label>
          <input type="radio" name="rbcidade" id="rbcidade" value="jlle">
          <label for="radiocidade">Mora em Curitiba:</label>
          <input type="radio" name="rbcidade" id="rbcidade" value="cwb">
        </p>
        <p>
          <label for="arquivo">Arquivo:</label>
          <input type="file" name="arquivo" id="arquivo">
        </p>
        <p>
          <label for="selecao">Seleção:</label>
          <select name="selecao" id="selecao">
            <optgroup label="numeros">
              <?php for($i=0;$i<10;$i++) { ?><option><?=$i ?></option> <?php } ?>
          </select>
          <!-- 
          <select name="selcidade">
            <optgroup label="cidades">
              <option selected>Joinville</option>
              <option>Jaragua</option>
              <option>Mafra</option>
          </select> 
          -->
        </p>
        <p>
          <label for="textao">Textão:</label>
          <textarea rols=10 cols=20 name="textao" id="textao"> </textarea>
        </p>
      </fieldset>
      
      <fieldset>
        <legend>Suas preferências</legend>
      </fieldset>
      <input type="submit">
      <input type="reset" value="Limpar">
    </form>
  </body>
</html>