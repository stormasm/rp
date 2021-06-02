
To figure out where the logging is
```rust
rg logger
```

RustPython uses env_logger

```rust
RUST_LOG=info cargo run --example parse_folder /j/tmp32/python-examples/simple
RUST_LOG=debug cargo run --example parse_folder /j/tmp32/python-examples/simple
```

see examples/parse_folder.rs for more details on how to initialize
the logging machinery.

```rust
fd macros.rs
```

yields -> vm/src/macros.rs
