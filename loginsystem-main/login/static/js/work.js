function send(){
            
    var username=document.getElementById('username').value
    var password=document.getElementById('password').value
    var email=document.getElementById('email').value
    var phone=document.getElementById('phone').value

    console.log(username)
    var blobFile = $('#myfile').files[0];
    var formData = new FormData();
    formData.append("fileToUpload", blobFile);

    $.ajax({
       url: "/ajax/signup/",
       type: "POST",
       data: {
           'pro_image':formData,
           'username':username,
           'password':password,
           'phone':phone,
           'email':email,
       },
       dataType: 'json',
       success: function(data) {
           console.log(data)
        
       },
       
    });
    
    

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
function upload_img(){
    username=document.getElementById('username').value
    password=document.getElementById('password').value
    email=document.getElementById('email').value
    phone=document.getElementById('phone').value

    window.location.href='/image_upload?username='+username+"&password="+password+"&email="+email+"&phone="+phone;
}
