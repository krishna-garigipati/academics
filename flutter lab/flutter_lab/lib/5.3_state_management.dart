import 'package:flutter/material.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: SetStateCounter(),
    );
  }
}

class SetStateCounter extends StatefulWidget {
  @override
  _SetStateCounterState createState() => _SetStateCounterState();
}

class _SetStateCounterState extends State<SetStateCounter> {
  int _count = 0;

  void _increment() {
    setState(() {
      _count++;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('State Management: SetState')),
      body: Center(
        child: Text('Count: $_count', style: TextStyle(fontSize: 32)),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: _increment,
        child: Icon(Icons.add),
      ),
    );
  }
}