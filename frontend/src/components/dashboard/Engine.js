import React, { useState } from "react";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Container from "react-bootstrap/Container";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";
import { DivisionTable } from "./DivisionTable";
import { TrendChart } from "./TrendChart";
const Engine = () => {
  const [amount, setAmmount] = useState(5000);
  const [strategy, setStrategy] = useState();
  const [suggestions, setSuggestions] = useState([]);
  //   const onSubmit = (e) => {
  //     e.preventDefault();
  //   };

  return (
    <Container fluid>
      <Row style={{ minHeight: "25vh" }}>
        <Col xs={6}>
          <Row>
            <Form>
              <Row className="mb-3">
                <Form.Group as={Col} controlId="formGridEmail">
                  <Form.Label>Amount</Form.Label>
                  <Form.Control
                    type="text"
                    placeholder="Enter amount min 5000$"
                    value={amount}
                    onChange={(e) => {
                      setAmmount(e.target.value);
                    }}
                  />
                </Form.Group>

                <Form.Group as={Col} controlId="formGridPassword">
                  <Form.Label>Choose Investment Strategy:</Form.Label>
                  <Form.Select
                    as={Col}
                    aria-label="Default select example"
                    value={strategy}
                    onChange={(e) => {
                      setStrategy(e.target.value);
                    }}
                  >
                    <option value="undefined">Select an investing type</option>
                    <option value="1">Index</option>
                    <option value="2">Quality</option>
                    <option value="3">Value</option>
                    <option value="4">Ethical</option>
                    <option value="5">Growth</option>
                  </Form.Select>
                </Form.Group>
              </Row>
              <Button
                variant="primary"
                type="button"
                style={{ width: "100%" }}
                disabled={!strategy || !(strategy !== "undefined") || !amount}
              >
                Get Suggestion
              </Button>
            </Form>
          </Row>
        </Col>
        <Col xs={6}>
          <TrendChart
            trenddata={
              [
                // { x: 1, y: 2 },
                // { x: 2, y: 3 },
                // { x: 3, y: 5 },
                // { x: 4, y: 4 },
                // { x: 5, y: 6 },
              ]
            }
          />
        </Col>
        <div className="vertical"></div>
        <hr></hr>
      </Row>

      <Row style={{ minHeight: "25vh" }}>
        <Col xs={6}>
          <DivisionTable data={suggestions}></DivisionTable>
        </Col>
      </Row>
    </Container>
  );
};
export default Engine;
