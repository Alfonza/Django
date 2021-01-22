function send(){
            
    username=document.getElementById('username').value
    password=document.getElementById('password').value
    phonenum=document.getElementById('phonenum').value
    if(username=="" || password==""||phonenum==""){
        return 
    }
    window.location.href='/signup?username='+username+"&password="+password+"&phonenum="+phonenum;
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