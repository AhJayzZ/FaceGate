import '../css/navigateBar.css';
import Container from 'react-bootstrap/Container';

import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown';


function NavigateBar() {
  return (
    <div>
      <Navbar bg="primary" expand="lg" className='navBar'>
        <Container>
          <Navbar.Brand href="/" className='navBrand'>Wireless IoT</Navbar.Brand>
          <Navbar.Toggle aria-controls="basic-navbar-nav" />
          <Navbar.Collapse id="basic-navbar-nav">
            <Nav className="navDropdown">
              <NavDropdown title="選項">
                <NavDropdown.Item href="/">狀態</NavDropdown.Item>
              </NavDropdown>
            </Nav>
          </Navbar.Collapse>
        </Container>
      </Navbar>
    </div>
  );
}

export default NavigateBar;
