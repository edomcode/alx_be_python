#Ask the user for the weather
weather = input("what's the weather like today? (sunny/rain/cold): ").strip().lower()
#Make decisions based on the input
if weather =="sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather =="rain":
    print("Don't forget your umberlla and a raincoat.")
elif weather =="cold":
    print("Make sure to wear a warm coat and scarf.")
else:
    print("sorry, i don't have reccomendations for this weather.")
   