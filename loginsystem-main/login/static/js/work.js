function send(){
            
    username=document.getElementById('username').value
    password=document.getElementById('password').value
    email=document.getElementById('email').value
    phone=document.getElementById('phone').value
    regex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/ ;
    if(username=="" || password==""||phone==""||email==""){
        return 
    }
    if(email.match(regex)){
        window.location.href='/signup?username='+username+"&password="+password+"&email="+email+"&phone="+phone;
    }
    else{
        return
    }

}
function backhm(){
    window.location.href='back'
}
function logout(){
    window.location.href='logout'
}
function edit(){
    document.getElementById('edit_username').style.display="None"
    element=document.getElementById('username')
    input=document.createElement('input')
    input.value='{{user.name}}'
    element.innerHTML=""
    element.appendChild(input)
}
function update(field){
    new_value=input.value
    //window.location.href='update_profile?type='+field+'&newdata='+new_value+'&email='+user.email;
    
}
function back(){
    window.location.href='admin'
}

function send_update(){
    val1=document.getElementById('username').value
    val2=document.getElementById('password').value
    val3=document.getElementById('phone').value
    window.location.href='update_profile?email='+email+'&username='+val1+'&password='+val2+'&phone='+val3;
}
