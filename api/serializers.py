'''
Serializers allow complex data such as querysets and model instances to be converted to native Python datatypes
that can then be easily rendered into JSON, XML or other content types. 
Serializers also provide deserialization, allowing parsed data to be converted back into complex types,
after first validating the incoming data.

we can create and Update through serializers. Delete via serializers does not make any sense. we can delete directly python objects.

Creating Object using serializers

data={"title":"Abc","description:"asdfsa","price":789}
serialized_data=Adserializer(data)
serialized_data.is_valid()   
seriaized_data.save()

Please Note that save() can only be called once is_valid() is called and it had returned true

Updating Object using serializers

data={"title":"XYZ"}
obj=Ad.objects.first()
serialized_data=Adserializer(obj,data)
serialized_data.is_valid()   
seriaized_data.save()

Please Note you need to send all the fields for which blank is set false in model.

'''
from rest_framework import serializers

from .models import Ad

class Adserializer(serializers.ModelSerializer):
    class Meta:
        model=Ad
        fields=["title","description","price","images","subcatagory"]
        
    def validate_title(self,value): #For Validating Particular Field syantax: validate_<fieldname>(self,value):
        if len(value)<=10:
            raise serializers.ValidationError("Title too short!!")
        return value
    
    def validate(self,data): #For Validating Entire serializer object syntax validate(self,data):
        price=data.get("price",0)
        if(price<=0):
            raise serializers.ValidationError("Price Must be greater than 0")
        images=data.get("images",[])
        if(len(images)==0):
            raise serializers.ValidationError("No Images Provided")
        else:
            for img in images:
                if(not (img.startswith("http://") or img.startswith("https://") ) ):
                    raise serializers.ValidationError("One or More Invalid Image URL")
        return data