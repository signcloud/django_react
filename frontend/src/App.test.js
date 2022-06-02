import React from 'react';
import { render } from '@testing-library/react';
import Todo from './Todo';

test('renders learn react link', () => {
  const { getByText } = render(<Todo />);
  const linkElement = getByText(/learn react/i);
  expect(linkElement).toBeInTheDocument();
});
