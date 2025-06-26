-- Create order_header table
CREATE TABLE order_header (
    order_id CHAR(10) PRIMARY KEY,
    total_amount DECIMAL(10, 2) NOT NULL,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
);

COMMENT ON TABLE order_header IS 'This table contains only information about the order header.';
COMMENT ON COLUMN order_header.order_id IS 'Unique identifier for the order.';
COMMENT ON COLUMN order_header.total_amount IS 'Total amount for the order.';
COMMENT ON COLUMN order_header.order_date IS 'Timestamp when the order was created.';

-- Create order_item table
CREATE TABLE order_item (
    order_id CHAR(10) NOT NULL,
    order_item_id CHAR(4) NOT NULL,
    unit_price DECIMAL(10,2) NOT NULL,
    order_item_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    PRIMARY KEY (order_id, order_item_id),
    FOREIGN KEY (order_id) REFERENCES order_header(order_id) ON DELETE CASCADE
);

COMMENT ON TABLE order_header IS 'This table contains only information about the order header.';
COMMENT ON COLUMN order_header.order_id IS 'Unique identifier for the order.';
COMMENT ON COLUMN order_header.total_amount IS 'Total amount for the order.';
COMMENT ON COLUMN order_header.order_date IS 'Timestamp when the order was created.';
