import 'package:flutter/material.dart';

void main() => runApp(
  MaterialApp(
    // initialRoute = '/',
    routes: {
      '/': (context) => Scaffold(
        appBar: AppBar(title: const Text('Home Screen')),
        body: Center(
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              ElevatedButton(
                child: const Text('Go to screen 1'),
                onPressed: () {
                  Navigator.pushNamed(context, '/screen1');
                },
              ),
              const SizedBox(height: 20),

              ElevatedButton(
                child: const Text('Go to screen 2'),
                onPressed: () {
                  Navigator.pushNamed(context, '/screen2');
                },
              ),

              const SizedBox(height: 20),

              ElevatedButton(
                child: const Text('Go to screen 3'),
                onPressed: () {
                  Navigator.pushNamed(context, '/screen3');
                },
              ),
            ],
          ),
        ),
      ),

      '/screen1': (context) => Scaffold(
        appBar: AppBar(title: const Text('Screen 1')),
        body: Center(
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              ElevatedButton(
                child: const Text('Go to Home'),
                onPressed: () {
                  Navigator.pushNamed(context, '/');
                },
              ),
              const SizedBox(height: 20),

              ElevatedButton(
                child: const Text('Go to screen 2'),
                onPressed: () {
                  Navigator.pushNamed(context, '/screen2');
                },
              ),

              const SizedBox(height: 20),

              ElevatedButton(
                child: const Text('Go to screen 3'),
                onPressed: () {
                  Navigator.pushNamed(context, '/screen3');
                },
              ),
            ],
          ),
        ),
      ),

      '/screen2': (context) => Scaffold(
        appBar: AppBar(title: const Text('Screen 2')),
        body: Center(
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              ElevatedButton(
                child: const Text('Go to Home'),
                onPressed: () {
                  Navigator.pushNamed(context, '/');
                },
              ),
              const SizedBox(height: 20),

              ElevatedButton(
                child: const Text('Go to screen 1'),
                onPressed: () {
                  Navigator.pushNamed(context, '/screen1');
                },
              ),

              const SizedBox(height: 20),

              ElevatedButton(
                child: const Text('Go to screen 3'),
                onPressed: () {
                  Navigator.pushNamed(context, '/screen3');
                },
              ),
            ],
          ),
        ),
      ),

      '/screen3': (context) => Scaffold(
        appBar: AppBar(title: const Text('Screen 3')),
        body: Center(
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              ElevatedButton(
                child: const Text('Go to Home'),
                onPressed: () {
                  Navigator.pushNamed(context, '/');
                },
              ),
              const SizedBox(height: 20),

              ElevatedButton(
                child: const Text('Go to screen 1'),
                onPressed: () {
                  Navigator.pushNamed(context, '/screen1');
                },
              ),

              const SizedBox(height: 20),

              ElevatedButton(
                child: const Text('Go to screen 2'),
                onPressed: () {
                  Navigator.pushNamed(context, '/screen2');
                },
              ),
            ],
          ),
        ),
      ),
    },
  ),
);
