import 'package:flutter/material.dart';

void main() => runApp(
  MaterialApp(
    home: Scaffold(
      appBar: AppBar(title: const Text('First Screen')),
      body: Builder(
        builder: (context) {
          return Center(
            child: ElevatedButton(
              child: Column(
                mainAxisSize: MainAxisSize.min,
                children: [
                  const Text('Go to second screen'),
                  const SizedBox(height: 16),
                  Image.network(
                    'https://flutter.github.io/assets-for-api-docs/assets/widgets/owl.jpg',
                    width: 150,
                    height: 150,
                  ),
                ],
              ),
              onPressed: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (context) => Scaffold(
                      appBar: AppBar(title: const Text('Second Screen')),
                      body: Center(
                        child: ElevatedButton(
                          child: Column(
                            mainAxisSize: MainAxisSize.min,
                            children: [
                              const Text('Go back'),
                              const SizedBox(height: 16),
                              const Text('Hi'),
                              const Text('Bye'),
                              const Text('Namaste'),
                            ],
                          ),
                          onPressed: () {
                            Navigator.pop(context);
                          },
                        ),
                      ),
                    ),
                  ),
                );
              },
            ),
          );
        },
      ),
    ),
  ),
);
