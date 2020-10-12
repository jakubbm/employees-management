const urlGet =  "/messageboard/get";
const urlPost = `/messageboard/post`;
const container =  document.querySelector("#content");
const buttonPost  = document.querySelector("#post");
const userId = document.getElementById('user_id').textContent;
const csrftoken = getCookie('csrftoken');
let messagesNumber = 0;


function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}

function getFirstData(){
  fetch(urlGet)
      .then((resp) => resp.json())
      .then(function(data){
      let messages = data;
      messagesNumber = data.length
      console.log(messagesNumber);
      container.innerHTML='';
      for (i in messages){
          let date = messages[i].date.slice(0,10)
          let time = messages[i].date.slice(11,19)
          let backgroundColor = (i % 2 == 0) ? "evenpool":"oddpool";
          let content = `
              <div class="box ${backgroundColor}">
                <img src="${messages[i].profile_picture}" alt="">
                <div class="box-content">
                  <div class="box-title">${messages[i].employee_firstname} ${messages[i].employee_lastname}</div>
                  <div class="message">${messages[i].message}</div>
                </div>
                <div class="datebox">
                  ${date} ${time}
                </div>
              </div>`
        container.insertAdjacentHTML("afterbegin",content);
      };
    })
  }


  function getNextData(){
    fetch(urlGet)
        .then((resp) => resp.json())
        .then(function(data){
        let messages = data;
        let messagesNumberCheck = messages.length
        if (messagesNumber !== messagesNumberCheck){
          for (let i=messagesNumber; i<messagesNumberCheck; i++){
            let date = messages[i].date.slice(0,10)
            let time = messages[i].date.slice(11,19)
            let backgroundColor = (i % 2 == 0) ? "evenpool":"oddpool";
            let content = `
                <div class="box ${backgroundColor}">
                  <img src="${messages[i].profile_picture}" alt="">
                  <div class="box-content">
                    <div class="box-title">${messages[i].employee_firstname} ${messages[i].employee_lastname}</div>
                    <div class="message">${messages[i].message}</div>
                  </div>
                  <div class="datebox">
                    ${date} ${time}
                  </div>
                </div>`
          container.insertAdjacentHTML("afterbegin",content);
        };
        messagesNumber = messagesNumberCheck
        }})}


  function sendData(){
    let input = document.getElementById("input")
    let message = input.value;
    input.value = "";
    fetch(urlPost,{
      method:'POST',
      headers: {
        'Content-type':'application/json',
        'X-CSRFToken':csrftoken,
      },
      body:JSON.stringify({'message':message,'userId':userId})
    });
    getFirstData();
  }


getFirstData();
setInterval(getNextData,5000);

buttonPost.addEventListener("click",sendData);
document.addEventListener("keypress",e => {
  if (e.key == "Enter"){
    sendData();
  };
});


