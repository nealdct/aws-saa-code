# Command to generate load on the ALB

***replace with your alb dns name***
```for i in {1..200}; do curl http://your-alb-address.com & done; wait```
