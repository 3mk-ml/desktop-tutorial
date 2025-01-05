<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sana'a university website design - project </title>
    <link rel="icon" href="images/logo.png" type="image/png">
    <link rel="stylesheet" href="style.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Yanone+Kaffeesatz:wght@200..700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.6.0/css/fontawesome.min.css">
<script src="https://kit.fontawesome.com/4d93cdabab.js" crossorigin="anonymous"></script>

</head>
<body>


    <section class="sub-header">
<nav>
    <a href="index.html"><img src="images/logo2.png"></a>
    <div class="nav-links" id="navLinks">
        <i class="fa fa-times" onclick="hideMenu()"></i>
        <ul>
            <li><a href="index.html">HOME</a></li>
            <li><a href="about.html">ABOUT</a></li>
            <li><a href="course.html">COURSES</a></li>
            <li><a href="login.html">LOGIN</a></li>
            <li><a href="contact.html">CONTACT</a></li>
        </ul>
    </div>
    <i class="fa fa-bars" onclick="showMenu()"></i>
    
</nav>
<h1>Register Now !</h1>
    </section>
  
 <section class="login-content">
<div class="row">
    <div class="content-left">
        <img src="images/grad.jpg">
        <h2>Our Certificate & Online Programs For 2024 </h2>
        <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. In, quis. Officiis iusto enim recusandae ex quaerat consequuntur veritatis exercitationem neque, eaque sit dolorem reiciendis in voluptatum, praesentium aliquid vero aperiam.</p>
        <br>
        <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Ea omnis ipsam provident debitis ullam ut dolore nam, esse magnam unde architecto velit qui temporibus consequuntur illo error laborum corrupti sapiente.</p>
        <br>
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolores quis corporis qui, velit sapiente soluta praesentium reprehenderit quam deleniti numquam deserunt modi facilis tempore nostrum hic corrupti minus aliquid error?</p>
        <br>
        <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. A ut odit est pariatur excepturi expedita at mollitia officia, ipsum distinctio quam, fugiat minus atque assumenda cupiditate blanditiis magnam dolores laudantium.</p>
        <br>
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Nam aspernatur quasi debitis porro. A quia impedit ex velit voluptatibus enim distinctio ducimus doloremque voluptatem, consectetur rem alias maiores laborum dolorem?</p>
        <div class="login-box">
            <h3>Login To Your Account</h3>

            <?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    if (empty($_POST["name"])) {
        echo "enter the name !";
    } elseif (empty($_POST["email"])) {
        echo "enter the email !";
    } elseif (empty($_POST["password"])) {
        echo "enter the password !";
    } else {
        echo $_POST["password"];
    }
}
?>

            <form class="login-form" method="POST">
                <input type="text" placeholder="Enter The Name" name="name"><br>
                <input type="email" placeholder="Enter The Email" name="email"><br>
                <input type="password" placeholder="Enter The password" name="password"><br>
                <button class="hero-btn red-btn" name="login">Login</button>
            </form>

        </div>

    </div>
    <div class="content-right">
        <h3>Catagories</h3>
        <div>
            <span>Business Analytics</span>
            <span>21</span>
        </div>
        <div>
            <span>Data Sience</span>
            <span>28</span>
        </div>
        <div>
            <span>Information Technolegy</span>
            <span>45</span>
        </div>
        <div>
            <span>Computer Science</span>
            <span>42</span>
        </div>
        <div>
            <span>Artificial Intellegence</span>
            <span>33</span>
        </div>
    </div>
    


</div>




 </section>


   
    




<section class="footer">
    <h4>About Us</h4>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Reprehenderit sunt, ab architecto odio distinctio tenetur<br> cumque autem animi tempore nihil! Voluptatum architecto magnam vel qui?</p>
    
    <div class="icons">
        <i class="fa fa-facebook"></i>
        <i class="fa fa-twitter"></i>
        <i class="fa fa-instagram"></i>
        <i class="fa fa-linkedin"></i>
    </div>
</section>

<script src="script.js">
      
</script>
</body>
</html>