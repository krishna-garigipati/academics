
import 'package:flutter/material.dart';

void main() => runApp(
  MaterialApp(
    debugShowCheckedModeBanner: false,
    home: Scaffold(
      appBar: AppBar(title: const Text('Simple Responsive UI')),
      body: LayoutBuilder(
        builder: (context, constraints) {
          final width = constraints.maxWidth;
          String text = 'Mobile View';
          IconData icon = Icons.phone_android;
          double fontSize = 24;

          if (width >= 600 && width < 1200) {
            text = 'Tablet View';
            icon = Icons.tablet_android; // more DartPad-compatible
            fontSize = 28;
          } else if (width >= 1200) {
            text = 'Desktop View';
            icon = Icons.desktop_mac; // changed to fix potential icon issues
            fontSize = 32;
          }

          return Center(
            child: Column(
              mainAxisSize: MainAxisSize.min,
              children: [
                Icon(icon, size: 80),
                const SizedBox(height: 20),
                Text(text, style: TextStyle(fontSize: fontSize)),
              ],
            ),
          );
        },
      ),
    ),
  ),
);
