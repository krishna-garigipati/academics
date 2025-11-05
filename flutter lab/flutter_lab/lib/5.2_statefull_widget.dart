import 'package:flutter/material.dart';

void main() => runApp(MaterialApp(home: Counter()));

class Counter extends StatefulWidget{
    @override
    _CounterState createState() => _CounterState();
}

class _CounterState extends State<Counter>{
    int count = 0;

    @override
    Widget build(BuildContext context){
        return Center(
            child: TextButton(
                onPressed: () => setState(() => count++),
                child: Text('Count: $count', style: TextStyle(fontSize: 24)),
            ),
        );
    }
}