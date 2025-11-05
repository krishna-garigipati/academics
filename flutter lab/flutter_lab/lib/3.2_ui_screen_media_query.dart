import 'package:flutter/material.dart';

void main() => runApp(
  MaterialApp(
    home: Scaffold(
     appBar: AppBar(title: Text("Responsive building using Media Queries")),
     
     body: Builder(
      builder: (context){
        final width = MediaQuery.of(context).size.width;
        String text = 'Small Screen';
        IconData icon = Icons.phone_android;
        double fontSize = 24;
        
        if (width >= 600 && width < 1200) {
            text = 'Medium Screen';
            icon = Icons.tablet_android; 
            fontSize = 28;
        } 
        
        else if (width >= 1200) {
            text = 'Large Screen';
            icon = Icons.desktop_mac; 
            fontSize = 32;
        }
        
        return Center(
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              Icon(icon, size: 80),
              const SizedBox(height: 20),
              Text(text, style: TextStyle(fontSize: fontSize)),
              const SizedBox(height: 10),
              Text('Screen Width: ${width.toStringAsFixed(0)} px')
            ],
          ),
        );
      },
     ),
    ),
  ),
);
