# cherrypie-ssl-errors

I am creating this so @cherrpy on Twitter can help debug. I receive ssl.bad.tick() errors. Or something along those lines. I already rm'd the log files and went back to the ancient HTTP protocol since I cannot figure this out. Here is a copy/paste of one of the errors I am receiving: ENGINE Error in HTTPServer.tick and ssl.SSLError: [SSL: SSLV3_ALERT_BAD_CERTIFICATE] sslv3 alert bad certificate (_ssl.c:1051) 

I receive the above error for about a week. The application works and then crashes. Then I restart the application from cron and anything input into the application server form field returns a 500 error. I am not posting the application source code now just the configuration that pertains to the SSL connection. I am using LetsEncrypt certificates that come with my domain. 

Thank-you for reading this. :)
