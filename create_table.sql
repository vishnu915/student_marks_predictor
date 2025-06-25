CREATE DATABASE IF NOT EXISTS student_prediction;
USE student_prediction;

CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    roll_no VARCHAR(20),
    hours_studied FLOAT,
    predicted_marks FLOAT
);