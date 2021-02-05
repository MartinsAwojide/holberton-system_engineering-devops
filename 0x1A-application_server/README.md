# 0x1A Application server

> Using a shell script is most useful for repetitive tasks that may be time consuming to execute by typing one line at a time. A few examples of applications shell scripts can be used for include: Automating the code compiling process. Running a program or creating a program environment. This project covers deploying the application server in  real environemnt.

At the end of this project, I was able to solve these questions:

Your web infrastructure is already serving web pages via Nginx that you installed in your first web stack project. While a web server can also serve dynamic content, this task is usually given to an application server. In this project you will add this piece to your infrastructure, plug it to your Nginx and make is serve your Airbnb clone project.


## Tasks

0. Nginx config file to serve a page from the route /airbnb-onepage/
1. Nginx config file by adding another service for Gunicorn to handle. In AirBnB_clone_v2/web_flask/6-number_odd_or_even, the route /number_odd_or_even/<int:n>
2. Nginx config file must serve a page both locally and on its public IP on port 80
