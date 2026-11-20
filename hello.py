tools=[
    {"name":"search","priority":3},
    {"name":"calculator","priority":1},
]
sorted(tools,key=lambda t:t["priority"])
