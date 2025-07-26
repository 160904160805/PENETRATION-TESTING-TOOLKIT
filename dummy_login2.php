<?php
// dummy_login2.php
$correct_user = "root";
$correct_pass = "qwerty123";

$message = "";

if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $input_user = $_POST["username"] ?? "";
    $input_pass = $_POST["password"] ?? "";

    if ($input_user === $correct_user && $input_pass === $correct_pass) {
        $message = "Login success";
    } else {
        $message = "Invalid credentials";
    }
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Dummy Login 2</title>
</head>
<body>
    <h2>🔒 Dummy Login Page 2</h2>

    <form method="POST" action="">
        <label>Username:</label><br>
        <input type="text" name="username"><br><br>

        <label>Password:</label><br>
        <input type="password" name="password"><br><br>

        <button type="submit">Login</button>
    </form>

    <p><?= $message ?></p>
</body>
</html>
