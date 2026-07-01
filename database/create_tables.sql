CREATE DATABASE IF NOT EXISTS loan_management;
USE loan_management;

CREATE TABLE active_loans (
    Active_ID VARCHAR(20) PRIMARY KEY,
    Loan_Date DATE,
    Customer_Name VARCHAR(100),
    Amount DECIMAL(10,2),
    Interest_Rate DECIMAL(5,2),
    Status VARCHAR(20)
);

CREATE TABLE released_loans (
    Book_No VARCHAR(20) PRIMARY KEY,
    Loan_Date DATE,
    Release_Date DATE,
    Customer_Name VARCHAR(100),
    Principal_Amount DECIMAL(10,2),
    Interest_Rate DECIMAL(5,2),
    Interest_Earned DECIMAL(10,2),
    Status VARCHAR(20)
);