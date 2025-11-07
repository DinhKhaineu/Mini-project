CREATE DATABASE IF NOT EXISTS university CHARSET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE university;

DROP TABLE IF EXISTS students;
CREATE TABLE students (
  student_id      INT PRIMARY KEY AUTO_INCREMENT,
  full_name       VARCHAR(100) NOT NULL,
  dob             DATE,
  gender          ENUM('M','F') NOT NULL,
  major           VARCHAR(50),
  class_id        VARCHAR(20),
  email           VARCHAR(120),
  phone           VARCHAR(20),
  gpa             DECIMAL(3,2),
  credits         INT,
  height_cm       DECIMAL(5,2),
  weight_kg       DECIMAL(5,2),
  province        VARCHAR(60),
  enrollment_date DATE
);

INSERT INTO students (full_name, dob, gender, major, class_id, email, phone, gpa, credits, height_cm, weight_kg, province, enrollment_date) VALUES
('Nguyen Van A','2004-05-12','M','Data Science','DS01','a.nguyen@neu.edu.vn','0911000001',3.50,80,175.0,68.0,'Ha Noi','2022-09-05'),
('Tran Thi B','2003-11-02','F','AI','AI01','b.tran@neu.edu.vn','0911000002',3.85,95,160.0,50.0,'Hai Phong','2021-09-06'),
('Le Van C','2004-07-20','M','Data Science','DS02','c.le@neu.edu.vn','0911000003',2.10,40,180.0,95.0,'Thai Nguyen','2022-09-05'),
('Pham Thi D','2003-01-30','F','Business Analytics','BA01','d.pham@neu.edu.vn','0911000004',NULL,70,158.0,48.0,'Nam Dinh','2021-09-06'),
('Hoang Van E','2004-09-10','M','AI','AI02','e.hoang@neu.edu.vn','0911000005',3.95,110,170.0,120.0,'Ha Noi','2022-09-05'),
('Vu Thi F','2005-03-08','F','Data Science','DS01','f.vu@neu.edu.vn','0911000006',3.20,75,165.0,52.0,'Ha Nam','2023-09-04'),
('Do Van G','2003-12-25','M','Business Analytics','BA02','g.do@neu.edu.vn','0911000007',2.70,60,NULL,70.0,'Ninh Binh','2021-09-06'),
('Bui Thi H','2004-06-18','F','AI','AI01','h.bui@neu.edu.vn','0911000008',3.10,65,155.0,NULL,'Hung Yen','2022-09-05'),
('Pham Van I','2005-02-22','M','Data Science','DS02','i.pham@neu.edu.vn','0911000009',1.80,30,172.0,60.0,'Thanh Hoa','2023-09-04'),
('Nguyen Thi J','2004-08-14','F','Business Analytics','BA01','j.nguyen@neu.edu.vn','0911000010',3.60,100,162.0,54.0,'Ha Noi','2022-09-05');
SHOW TABLES;         -- lists all tables
DESCRIBE students; -- shows the structure (columns, types, keys)
SELECT * FROM students -- displays the data inside
