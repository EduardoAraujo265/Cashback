function carregarConsultas() {
  fetch('/consultas')
    .then(response => response.json())      
    .then(json => {
      const todos = Object.values(json);
      const tbody = document.getElementById('table-body');
      tbody.innerHTML = '';

      todos.forEach(consulta => {
       
          let { vip, valor, cashback} = consulta; 
          const row = document.createElement('tr');
          row.innerHTML = `
            <td>${vip}</td>
            <td>${valor}</td>
            <td>${cashback}</td>
          `;
          tbody.appendChild(row);
        });
    });
}

const botaoConsultar = document.getElementById('consultar');
botaoConsultar.addEventListener('click',() => {
  const bodyrequest = {
    "valor": parseFloat(document.getElementById('inputValor').value),
    "vip": document.getElementById('inputVip').value
  };
  console.log("bodyrequest", bodyrequest);
    fetch('/cashback', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(bodyrequest)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Cashback Calculado:', data);
        carregarConsultas();
    })
    .catch(error => console.error('Erro ao calcular cashback:', error));
})
  


addEventListener('DOMContentLoaded', () => {
    
    const myDiv = document.querySelector('#mydiv');
    const table = document.createElement('table');
    table.innerHTML = `
      <thead>
          <tr>
              <th>Vip</th>
              <th>Valor da compra</th>
              <th>Cashback</th>
          </tr>
      </thead>
      <tbody id="table-body">
      </tbody>
    `;
    myDiv.appendChild(table);
    carregarConsultas();
});