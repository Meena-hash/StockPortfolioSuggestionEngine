import React from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faDatabase } from "@fortawesome/free-solid-svg-icons";
import Container from "react-bootstrap/esm/Container";
export const DivisionTable = ({ data }) => {
  return data && data.length !== 0 ? (
    <table className="ui celled table">
      <thead>
        <tr>
          <th>Stock Symbol</th>
          <th>Stock Name</th>
          <th>Current Price</th>
          <th>Number of shares</th>
          <th>Total Cost</th>
        </tr>
      </thead>

      <tbody>
        {Object.keys(data).map((rec) => {
          return (
            <tr>
              <td data-label="Stock Symbol">{data[rec].symbol}</td>
              <td data-label="Stock Name">{data[rec].name}</td>
              <td data-label="Current Price" className="ui red text">
                <div className="ui mini statistics">
                  <div className="statistic">
                    <div className="value">{data[rec].price}</div>
                    <div className="label">USD</div>
                  </div>
                  {data[rec].increase_dollars > 0 ? (
                    <div className="green statistic">
                      <div className="value">
                        <i className="long arrow alternate up icon"></i>
                        {`${data[rec].increase_dollars} (${data[rec].increase_percent}%)`}
                      </div>
                    </div>
                  ) : (
                    <div className="red statistic">
                      <div className="value">
                        <i className="long arrow alternate down icon"></i>
                        {`${data[rec].increase_dollars} (${data[rec].increase_percent}%)`}
                      </div>
                    </div>
                  )}
                </div>
              </td>
              <td data-label="Number of shares">
                {data[rec].cost / data[rec].price}
              </td>
              <td data-label="Total Cost">{data[rec].cost}</td>
            </tr>
          );
        })}
      </tbody>
    </table>
  ) : (
    <Container
      style={{
        display: "flex",
        width: "60%",
        justifyContent: "center",
        alignItems: "center",
        height: "25vh",
        margin: "0 auto",
      }}
    >
      <FontAwesomeIcon icon={faDatabase} size="4x" />
    </Container>
  );
};
export default DivisionTable;
