import 'package:flutter/material.dart';

void main() =>
    runApp(MaterialApp(home: Center(child: Container(
      padding: EdgeInsets.all(24),
      decoration: BoxDecoration(
        border: Border.all(color: Colors.red, width: 2),
        borderRadius: BorderRadius.circular(12),
      ),
      child: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          Icon(Icons.star, size: 48, color: Colors.amber),
          Text('Hello, Stateless Widget!'),
        ],
      ),
))));
