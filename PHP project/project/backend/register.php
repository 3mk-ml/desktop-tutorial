<?php
require 'config/db.php';

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $name = $_POST['name'];
    $email = $_POST['email'];
    $password = password_hash($_POST['password'], PASSWORD_BCRYPT);
    $user_type = 'admin'; // Default user type

    $stmt = $pdo->prepare("INSERT INTO users (name, email, password, user_type) VALUES (?, ?, ?, ?)");
    $stmt->execute([$name, $email, $password, $user_type]);

    header('Location: login.php');
    exit;
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register</title>
    <link rel="stylesheet" href="../frontend/style.css">
</head>
<body>
    <section class="sub-header">
        <nav>
            <a href="../frontend/index.php"><img src="../frontend/images/logo2.png"></a>
            <div class="nav-links" id="navLinks">
                <i class="fa fa-times" onclick="hideMenu()"></i>
                <ul>
                    <li><a href="../frontend/index.php">HOME</a></li>
                    <li><a href="../frontend/about.php">ABOUT</a></li>
                    <li><a href="../frontend/course.php">COURSES</a></li>
                    <li><a href="login.php">LOGIN</a></li>
                    <li><a href="../frontend/contact.php">CONTACT</a></li>
                </ul>
            </div>
            <i class="fa fa-bars" onclick="showMenu()"></i>
        </nav>
        <h1>Register</h1>
    </section>

    <section class="login-content">
        <div class="row">
            <div class="content-left">
                <form method="POST" action="register.php">
                    <input type="text" name="name" placeholder="Enter Your Name" required><br>
                    <input type="email" name="email" placeholder="Enter Your Email" required><br>
                    <input type="password" name="password" placeholder="Enter Your Password" required><br>
                    <button type="submit" class="hero-btn red-btn">Register</button>
                </form>
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

    <script src="../frontend/script.js"></script>
</body>
</html>