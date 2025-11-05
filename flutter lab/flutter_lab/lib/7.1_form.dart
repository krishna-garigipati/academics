import 'package:flutter/material.dart';

void main() => runApp(MaterialApp(home: SimpleForm()));

class SimpleForm extends StatefulWidget{
    @override
    _SimpleFormState createState() => _SimpleFormState();
}

class _SimpleFormState extends State<SimpleForm>{
    final _formKey = GlobalKey<FormState>();
    String name = "";
    String email = "";
    String password = "";
    String gender = 'Male';
    bool accepted = false;

    final genders = ['Male', 'Female', 'Other'];

    @override
    Widget build(BuildContext context){
        return Scaffold(
            appBar: AppBar(title: Text('Simple Form')),
            body: Padding(
                padding: EdgeInsets.all(16),
                child: Form(
                    key: _formKey,
                    child: ListView(
                        children: [
                            TextFormField(
                                decoration: InputDecoration(labelText: 'Name'),
                                onSaved: (val) => name = val?? "",
                                validator: (val) => val!.isEmpty ? 'Enter name: ':null,
                            ),

                            TextFormField(
                                decoration: InputDecoration(labelText: 'Email'),
                                keyboardType: TextInputType.emailAddress,
                                onSaved: (val) => email = val?? "",
                                validator: (val) => val!.contains('@') ? null : 'Enter a valid email',
                            ),

                            TextFormField(
                                decoration: InputDecoration(labelText: 'Password'),
                                obscureText: true,
                                onSaved: (val) => password = val ?? "",
                                validator: (val) => val!.length < 6 ? 'Min 6 characters':null,
                            ),

                            DropdownButtonFormField<String>(
                                value: gender,
                                items: genders.map((g) => DropdownMenuItem(value: g, child: Text(g))).toList(),
                                onChanged: (val) => setState(() => gender = val??'Male'),
                                decoration: InputDecoration(labelText: 'Gender'),
                            ),
                            
                            CheckboxListTile(
                                title: Text('Accept Terms'),
                                value: accepted,
                                onChanged: (val) => setState(() => accepted = val??false),
                            ),

                            ElevatedButton(
                                child: Text('Submit'),
                                onPressed: (){
                                    if(_formKey.currentState!.validate()&&accepted){
                                        _formKey.currentState!.save();
                                        showDialog(
                                            context: context,
                                            builder: (_) => AlertDialog(
                                                title: Text('Form Submitted'),
                                                content: Text('Name: $name\nEmail: $email\nGender: $gender'),
                                            ),
                                        );
                                    } else if(!accepted){
                                        ScaffoldMessenger.of(context).showSnackBar(
                                            SnackBar(content: Text('Please accept the terms'))
                                        );
                                    }
                                },
                            )
                        ]
                    )
                )
            )
        );
    }
}

