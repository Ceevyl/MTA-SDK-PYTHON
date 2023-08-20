# Python SDK Para o MTA ( Multi Theft Auto ) 

# Developed By Ceevyl

# How To Install
```
pip install MTA-SDK-Python
```

# How to Create 

```py
#             Using Url and Login & Pass
Client = Mta("http://localhost:22005", ( "Batata", 1234 )  )
                   
response = Client.call(  "resourceName", "functionName", ['Args1', 'Arg2...']  )

print(response.json())

```
