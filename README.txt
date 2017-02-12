Install nginx, supervisor, python-pip
Then using pip install flask and gunicorn to run the python flask app

Create a directory myapp under /root

Copy myapp.py to /root/myapp

Copy the supervisor config myapp.conf to /etc/supervisor/conf.d

Then restart supervisor service
service supervisor restart - restart supervisor service

Below are the supervisorctl commands to update the config, start and stop the supervisor jobs.

supervisorctl reread
supervisorctl update
supervisorctl start myapp
supervisorctl stop myapp
supervisorctl status

Copy the nginx config myapp to /etc/nginx/sites-enabled

Then restart nginx

service nginx stop
service nginx start
service nginx restart

So now the nginx config is routing the requests coming to <ip>:80 to the python flask app 
which is running on gunicorn port 5000