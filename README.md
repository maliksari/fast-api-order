###   Migration ları oluşturmak için
- alembic revision --autogenerate -m "init" 

###  Migrate için 
-  alembic upgrade head



<!-- ### Daha sonra mimariyi Güncelle

project
│   app.py
│   main.py
│
└───app
│   └───api
│   │   └───v1
│   │       └───endpoints
│   │           ├───products.py
│   │           ├───orders.py
│   │           ├───users.py
│   └───core
│   │   └───request_models
│   │       ├───products.py
│   │       ├───orders.py
│   │       ├───users.py
│   └───response_models
│       ├───products.py
│       ├───orders.py
│       ├───users.py -->
