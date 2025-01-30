<?php
session_start();
require 'config/db.php';

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $email = $_POST['email'];
    $password = $_POST['password'];

    $stmt = $pdo->prepare("SELECT * FROM users WHERE email = ?");
    $stmt->execute([$email]);
    $user = $stmt->fetch();

    if ($user && password_verify($password, $user['password'])) {
        $_SESSION['user_id'] = $user['id'];
        $_SESSION['user_type'] = $user['user_type'];
        header('Location: user/profile.php');
        exit;
    } else {
        echo "<script>alert('Invalid email or password.');</script>";
    }
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
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
        <h1>Login</h1>
    </section>

    <section class="login-content">
        <div class="row">
            <div class="content-left">
                <form method="POST" action="login.php">
                    <input type="email" name="email" placeholder="Enter Your Email" required><br>
                    <input type="password" name="password" placeholder="Enter Your Password" required><br>
                    <button type="submit" class="hero-btn red-btn">Login</button>
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